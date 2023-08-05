from txp.common.utils import firestore_utils
from txp.common.utils import bigquery_utils
import datetime
from txp.common.config import settings


def get_max_frequency_sections(bigquery_db, table_name, tenant_id, start_datetime, end_datetime,
                               max_frequency_section_type):
    max_frequency_sections = bigquery_utils.get_all_sections_within_interval(bigquery_db, table_name, tenant_id,
                                                                             start_datetime, end_datetime,
                                                                             max_frequency_section_type[0])
    if not max_frequency_sections:
        return None
    else:
        filtered_max_frequency_sections = filter_sections(start_datetime, end_datetime, max_frequency_sections)
        if filtered_max_frequency_sections:
            return filtered_max_frequency_sections
        else:
            return None


def filter_sections(start_datetime, end_datetime, sections):
    return [s for s in sections
            if datetime.datetime.strptime(s["start_timestamp"], settings.time.datetime_zoned_format)
            >= start_datetime and
            datetime.datetime.strptime(s["end_timestamp"],
                                       settings.time.datetime_zoned_format) <= end_datetime]


def get_report_sections(firestore_db, bigquery_db, table_name, tenant_id, report_id, start_datetime: datetime.datetime,
                        end_datetime: datetime.datetime):
    tenant_doc = firestore_utils.pull_tenant_doc(firestore_db, tenant_id).to_dict()
    reports = tenant_doc["reports"]
    sections = tenant_doc["sections"]
    report_sections = {section: sections[section]
                       for section in sections if section in reports[report_id]["sections"]}
    max_frequency_section_type = max(report_sections.items(), key=lambda x: x[1]["frequency"])

    max_frequency_sections = get_max_frequency_sections(bigquery_db, table_name, tenant_id, start_datetime,
                                                        end_datetime, max_frequency_section_type)
    report_end_datetime = max_frequency_sections[0]['creation_timestamp'].to_pydatetime()
    report_start_datetime = \
        max_frequency_sections[-1]['creation_timestamp'].to_pydatetime() - \
        datetime.timedelta(minutes=max_frequency_section_type[1]["frequency"])
    all_sections = []
    for section in report_sections:
        sections_within_interval = bigquery_utils.get_all_sections_within_interval(bigquery_db, table_name, tenant_id,
                                                                                   report_start_datetime,
                                                                                   report_end_datetime,
                                                                                   section)
        all_sections += filter_sections(report_start_datetime, report_end_datetime, sections_within_interval)
    return all_sections
