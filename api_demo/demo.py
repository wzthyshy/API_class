from api_keywords.keyword import KeyDemo
import configparser
import yaml
# 实例化需要的内容
conf = configparser.ConfigParser()
kd = KeyDemo()

# 创建data
file = open('../data/login.yaml', 'r')
data = yaml.load(file, yaml.FullLoader)
print(data)

# 测试数据
conf.read('../config/config.ini')
url = conf.get('DEFAULT', 'url') + data['path']

# 执行测试
res = kd.post(url=url, param=data['data'])
print(res.text)
