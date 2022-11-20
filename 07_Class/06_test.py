# 6、假设列表list_busstop=[‘蛟桥’，‘车管所’，‘农大东区’，‘财大’，‘下罗北’，‘下罗’，‘舍里甲’，‘城建学校’，
# ‘瀛上路口’，‘公交运输集团’，‘昌北’，‘儿童医院’，‘青山路口’]
# 存放了某公交线路途经的公交站名。试编写程序，根据用户输入的起始站和终点站名，计算需要途经的站数，并将结果输出。
# 例如，当输入起始站为‘财大’，终点站为‘城建学校’时，输出内容为“从财大站前往城建学校站需要4站路”；
# 当输入起点站为‘财大’，终点站为‘蛟桥’时，输出“您需要乘坐反方向线路”
# 当输入的站名不存在时，告知输错了。

list_busstop = ["蛟桥", "车管所", "农大东区", "财大", "下罗北", "下罗", "舍里甲", "城建学校", "瀛上路口", "公交运输集团", "昌北", "儿童医院", "青山路口"]
starSite = input("请用户输入起始站：")
endSite = input("请用户输入终点站：")
if starSite in list_busstop and endSite in list_busstop:
    indexS = list_busstop.index(starSite)
    indexE = list_busstop.index(endSite)
    if indexS > indexE:
        print("你需要乘坐反方向路线")
    else:
        print("从"+starSite+"站前往"+endSite+"站需要"+str((indexE-indexS))+"站")
else:
    print("你输入的站点不存在")

