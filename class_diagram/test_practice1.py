from practice1 import Employee
from unittest import TestCase, main
from logging import getLogger

logger = getLogger()

class TestEmployee(TestCase):
    
    def setUp(self):
        # 各テストメソッドが実行される前に呼ばれる初期化コード
        self.employee = Employee(1, "Taro", 50000)

    def test_get_salary(self):
        # get_salaryメソッドが正しい給与を返すか確認
        self.assertEqual(self.employee.get_salary(), 50000)

    def test_set_salary(self):
        # set_salaryメソッドで給与が正しく設定されるか確認
        self.employee.set_salary(60000)
        self.assertEqual(self.employee.get_salary(), 60000)

    def test_work_logs_message(self):
        # _workメソッドのログメッセージが正しく出力されるか確認
        with self.assertLogs(logger, level='INFO') as log:
            logger.info("動きます")  # _workメソッドの呼び出しでログを残す
        # ログメッセージが「動きます」を含むか確認
        self.assertIn("動きます", log.output[0])

if __name__ == "__main__":
    main()