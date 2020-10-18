from itemadapter import ItemAdapter


class DazhongPipeline:
    def open_spider(self, spider):
        print("数据开始录入")

    def close_spider(self, spider):
        print("数据已完成录入")
        print(spider.conn.smembers("dianPingShop"))

    def process_item(self, item, spider):
        ex = spider.conn.sadd('dianPingShop', item['title'])
        return item
