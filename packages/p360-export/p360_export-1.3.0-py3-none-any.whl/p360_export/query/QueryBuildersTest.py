import unittest
from p360_export.query.QueryBuilder import QueryBuilder
from pysparkbundle.test.PySparkTestCase import PySparkTestCase


CONFIG = {
    "params": {"export_columns": ["phone", "gen"], "mapping": {"EMAIL": "mapped_email"}},
    "segments": [
        {
            "definition_segment": [
                {
                    "attributes": [
                        {"op": "BETWEEN", "id": "col_1", "value": [0.0, 14.0]},
                        {"op": "LESS THAN", "id": "col_2", "value": 0.0},
                        {"op": "GREATER THAN", "id": "col_3", "value": 0.0},
                        {"op": "EQUALS", "id": "col_4", "value": 0.0},
                        {"op": "EQUALS", "id": "col_5", "value": ["a", "b"]},
                        {"op": "NOT_EQUALS", "id": "col_5", "value": 1.5},
                        {"op": "NOT_EQUALS", "id": "col_5", "value": ["c", "d"]},
                    ],
                    "op": "AND",
                }
            ],
        }
    ],
}
EXPECTED_CONDITIONS = """(
col_1 BETWEEN 0.0 AND 14.0
AND
col_2 < 0.0
AND
col_3 > 0.0
AND
col_4 = 0.0
AND
col_5 IN ('a','b')
AND
col_5 != 1.5
AND
col_5 NOT IN ('c','d')
);"""


class QueryBuildersTest(PySparkTestCase):
    def expected_query(self, table_id):
        return f"SELECT phone, gen, mapped_email FROM {table_id} WHERE\n" + EXPECTED_CONDITIONS

    def test_query_builder(self):
        query_builder = QueryBuilder()
        query, table_id = query_builder.build(CONFIG)
        self.assertEqual(query, self.expected_query(table_id))

    def test_exporting_all_users(self):
        query_builder = QueryBuilder()
        config = {"params": CONFIG["params"], "segments": [[]]}
        query, table_id = query_builder.build(config)
        self.assertEqual(query, f"SELECT phone, gen, mapped_email FROM {table_id};")


if __name__ == "__main__":
    unittest.main()
