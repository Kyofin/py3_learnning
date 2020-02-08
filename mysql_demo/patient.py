# 导入pymysql模块
"""
python3
连接mysql、将结果画图
"""
import pymysql
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
# 连接mysql数据库，查数据
def result():
    # 连接database
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="eWJmP7yvpccHCtmVb61Gxl2XLzIrRgmT",
                           database="test",
                           charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    # 定义要执行的SQL语句
    sql = """
     SELECT
    	patient_name,
    	COUNT( 1 ) c
    FROM
    	tb_cis_patient_info 
    GROUP BY
    	patient_name 
    ORDER BY
    	c DESC
    limit 10
    """
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 获取查询的所有记录
        results = cursor.fetchall()

        x = []  # 存储患者名
        y = []  # 存储患者名的数量
        for row in results:
            patient_name = row[0]
            count_patient = row[1]

            x.append(patient_name)  # 出版社
            y.append(count_patient)  # 数量
        return x, y  # 返回两个结果

    except Exception as e:
        raise e
    finally:
        cursor.close()  # 关闭连接


# 绘制图形，显示结果
def books_bar(x,y):

    # 创建图层
    fig = plt.figure()
    color = ['r', 'g', 'pink',
             'plum', 'salmon']  # 柱状 - 颜色
    plt.bar(range(len(x)), y, color=color)
    myfont = FontProperties(fname="/System/Volumes/Data/Users/huzekang/Documents/SimHei.ttf")
    # 设置x轴的刻度值 - -XXX出版社
    plt.xticks(range(len(x)), x)
    # 1- 刻度值重叠，刻度值进行旋转
    fig.autofmt_xdate(rotation=45)

    plt.xlabel("patient_name",fontproperties=myfont)
    plt.ylabel("patient_name_count",fontproperties=myfont)
    plt.title("patient_chart_model",fontproperties=myfont)

    # 2- 每一个条形，真实的数据值需要显示 - plt.text()
    # x_1 -x轴的索引   y_1 -y轴的值
    for x_1, y_1 in enumerate(y):
        plt.text(x_1-0.2, y_1+3, str(y_1))

    # 保存到文件
    plt.savefig('patient_hhy.png')
    plt.show()


if __name__ == '__main__':
    x, y = result()
    # print(x)
    # print(y)
    books_bar(x, y)
