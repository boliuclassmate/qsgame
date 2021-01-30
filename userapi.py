# -*- coding: UTF-8 -*-
from runner.extapi import *
# 添加用户封装
# from userlib.demo_lib import *
# TODO: write your code


def shasijc(*args, **kwargs):

    # 杀死进程 放置json文件
    # 关闭APP
    closeApp("com.tencent.tmgp.wuxia")
    # 推送文件
    pushFile2Device("TestConfig.json",r"/sdcard/Android/data/com.tencent.tmgp.wuxia/files")
    sleep(5)
    pushFile2Device("ServerConfig_Android_Retail.json",r"/sdcard/Android/data/com.tencent.tmgp.wuxia/files")
    sleep(5)
    # 启动app
    startApp("com.tencent.tmgp.wuxia", splashActivity='com.tencent.tmgp.wuxia.ApolloWuxia', timeOut=20)
    
    # 等待同意按钮
    wait('obj_1611714692141.jpg', timeOut=180)

    try:
        # 同意
        click('obj_1611714692141.jpg', position=(0.514, 0.796, 0.628, 0.873), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('同意')
    sleep(18)

        # 等待弹出更新
    while True:
        if exists('obj_1611717059062.jpg', timeOut=20, by=DriverType.CV):
            break
        else:
            sleep(12)
    sleep(8)

    try:
        # 资源更新
        click('obj_1611717059062.jpg', position=(0.512, 0.672, 0.651, 0.748), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('更新')
    sleep(12)

    while True:
        if exists('obj_1611717866283.jpg', timeOut=20, by=DriverType.CV):
            break
        else:
            click((0.917, 0.477), position=None)
            sleep(120)
    sleep(12)

    try:
        # 与QQ好友玩
        playWithQQFriends(locator = 'obj_1611717866283.jpg', acc = '', pwd = '', timeOut = 240)
    except:
        pass
    sleep(48)
    
    # 服务器列表加载

    try:
        # 关闭公告
        click('obj_1611719573073.jpg', position=(0.947, 0.237, 0.983, 0.3), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        try:
            click('obj_1611719611198.jpg', xOffset=0.075,yOffset=0.09, position=(0.825, 0.145, 0.953, 0.204))
        except:
            click((0.967, 0.267), position=None)
    sleep(12)

    while True:
        if exists('obj_1611718250245.jpg', timeOut=20, by=DriverType.CV):
            break
        else:
            sleep(12)

   
    try:
        # 更换
        click('obj_1611718214801.jpg', position=(0.587, 0.628, 0.631, 0.677), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        try:
            click('obj_1611718250245.jpg', xOffset=0.106,yOffset=-0.168, position=(0.416, 0.784, 0.585, 0.85))
        except:
            click((0.583, 0.652), position=None)
    sleep(6)

    # 我的服务器已有角色

    if exists('obj_1611891558816.jpg', timeOut=20, by=DriverType.CV):
        try:
            # QQ六区
            click('obj_1611890639254.jpg', position=(0.134, 0.749, 0.205, 0.811), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611890660734.jpg', xOffset=-0.142,yOffset=0.642, position=(0.249, 0.111, 0.333, 0.17))
            except:
                click((0.162, 0.787), position=None)
        sleep(5)
            
        try:
            # 1518
            click('obj_1611890697850.jpg', position=(0.272, 0.598, 0.372, 0.687), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611890717134.jpg', xOffset=0.145,yOffset=-0.009, position=(0.113, 0.563, 0.226, 0.731))
            except:
                click((0.295, 0.626), position=None)
        sleep(5)
    else:

        # 服务器没有角色信息
        try:
            # QQ六服
            click('obj_1611891292141.jpg', position=(0.132, 0.663, 0.209, 0.721), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611891352582.jpg', xOffset=-0.125,yOffset=0.536, position=(0.255, 0.118, 0.339, 0.186))
            except:
                click((0.173, 0.692), position=None)
            sleep(4)
        try:
            click('obj_1611895684793.jpg', xOffset=-0.009,yOffset=0.495, position=(0.256, 0.121, 0.333, 0.176))
        except:
            try:
                click('obj_1611901107970.jpg', xOffset=0.107,yOffset=-0.003, position=(0.137, 0.663, 0.215, 0.724))     # 2400
            except:    
                click((0.317, 0.692), position=None)
        sleep(4)

    try:
        # 闯荡江湖
        click('obj_1611719694080.jpg', position=(0.415, 0.784, 0.584, 0.852), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('闯荡江湖')
    sleep(24)

    if exists('obj_1611719794073.jpg', timeOut=20, by=DriverType.CV):
        # 不存在角色信息
        try:
            # 定制细节
            click('obj_1611719794073.jpg', position=(0.784, 0.858, 0.97, 0.944), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('定制细节')
        sleep(5)

        try:
            # 下一步
            click('obj_1611719839187.jpg', position=(0.815, 0.885, 0.969, 0.959), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('下一步')
        sleep(5)

        try:
            # 完成创建
            click('obj_1611719884049.jpg', position=(0.815, 0.885, 0.966, 0.962), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('完成创建')
        sleep(5)

        try:
            # 确定
            click('obj_1611719933971.jpg', position=(0.514, 0.598, 0.651, 0.669), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('确定')
        sleep(5)
        
        try:
            # 下一步
            click('obj_1611719980091.jpg', position=(0.813, 0.888, 0.969, 0.962), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('下一步')
        sleep(5)
    
        try:
            # 进入游戏
            click('obj_1611720014683.jpg', position=(0.787, 0.86, 0.964, 0.944), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('进入游戏')
        sleep(12)

        for i in range(18):
            if exists('obj_1611727738338.jpg', timeOut=240, by=DriverType.CV):
                try:
                    # 确认
                    click('obj_1611727738338.jpg', position=(0.452, 0.669, 0.544, 0.743), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
                except:
                    click_text('确认')
                sleep(120)
        sleep(4)

        for i in range(18):
            if exists('obj_1612005244511.jpg', timeOut=20, by=DriverType.CV) or exists('obj_1612005259982.jpg', timeOut=20, by=DriverType.CV):
                try:
                    # 2.5D 镜头
                    click((0.321, 0.499), position=None)
                    click((0.385, 0.443), position=None)
                    click((0.376, 0.292), position=None)
                except:
                    click((0.723, 0.482), position=None)
                sleep(6)
            sleep(12)

        try:
            click((0.321, 0.499), position=None)
            click((0.385, 0.443), position=None)
            click((0.376, 0.292), position=None)
        except:
            pass
        sleep(4)

        try:
            # 确定
            click('obj_1611720740536.jpg', position=(0.432, 0.779, 0.567, 0.842), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('确定')
        sleep(5)

        for i in range(18):
            if  exists('obj_1612005102624.jpg', timeOut=20, by=DriverType.CV):
                try:
                    # GM 
                    click('obj_1611895803478.jpg', xOffset=-0.002,yOffset=0.486, position=(0.047, 0.043, 0.074, 0.093))
                except:
                    try:
                        click('obj_1611895817787.jpg', position=(0.047, 0.539, 0.074, 0.576), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
                    except:
                        click((0.024, 0.558), position=None)
                sleep(12)
            sleep(12)

        try:
            # 声望 
            click('obj_1611920000238.jpg', xOffset=-0.633,yOffset=-0.582, position=(0.83, 0.74, 0.9, 0.882))
        except:
            try:
                #click('obj_1611822451293.jpg', position=(0.185, 0.193, 0.24, 0.27), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0) # 2400
                click('obj_1611919442501.jpg', xOffset=-0.71,yOffset=-0.533, position=(0.917, 0.74, 0.956, 0.783))
            except:    
                click((0.226, 0.23), position=None)
        sleep(12)

        try:
            # 等级提升至50
            click('obj_1612000720554.jpg', xOffset=-0.349,yOffset=-0.755, position=(0.833, 0.731, 0.896, 0.885))
        except:
            click((0.514, 0.023), position=None)
            click((0.512, 0.056), position=None)
            click((0.512, 0.082), position=None)
            click((0.408, 0.016), position=None)
            click((0.411, 0.049), position=None)
            click((0.409, 0.079), position=None)
            click((0.409, 0.105), position=None)
            click((0.506, 0.111), position=None)
        sleep(4)

        while True:
            if exists('obj_1611932170002.jpg', timeOut=20, by=DriverType.CV):
                break
            else:
                sleep(12)
        try:
            click('obj_1611932188392.jpg', position=(0.93, 0.019, 0.954, 0.068), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:  
                click('obj_1611932215155.jpg', xOffset=0.824,yOffset=-0.89, position=(0.062, 0.901, 0.159, 0.966))
            except:    
                click((0.939, 0.049), position=None)
        sleep(12)

        while True:
            if exists('obj_1612000297258.jpg', timeOut=20, by=DriverType.CV):
                break
            else:
                sleep(12)
        try:
            click('obj_1612000282494.jpg', position=(0.87, 0.003, 0.908, 0.102), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click('obj_1612000312234.jpg', xOffset=0.109,yOffset=-0.398, position=(0.731, 0.368, 0.827, 0.539))
        sleep(4)
    
    else:
        try:
            click('obj_1611910251261.jpg', position=(0.784, 0.861, 0.936, 0.947), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('进入游戏')
        sleep(48)
    
        if exists('obj_1611727738338.jpg', timeOut=240, by=DriverType.CV):
            try:
                # 确认
                click('obj_1611727738338.jpg', position=(0.452, 0.669, 0.544, 0.743), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
            except:
                click_text('确认')
        sleep(12)

    # 应用重启
    restart_app()
    sleep(4)

    # 测试环境
    try:
        # 确认
        click('obj_1611731203696.jpg', position=(0.405, 0.607, 0.598, 0.715), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('确定')
    sleep(4)

    while True:
        if exists('obj_1611719573073.jpg', timeOut=20, by=DriverType.CV):
            break
        else:
            sleep(12)
    sleep(4)

    try:
        # 关闭公告
        click('obj_1611719573073.jpg', position=(0.947, 0.237, 0.983, 0.3), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        try:
            click('obj_1611719611198.jpg', xOffset=0.075,yOffset=0.09, position=(0.825, 0.145, 0.953, 0.204))
        except:
            click((0.967, 0.267), position=None)
    sleep(12)

    try:
        # 闯荡江湖
        click('obj_1611719694080.jpg', position=(0.415, 0.784, 0.584, 0.852), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('闯荡江湖')
    sleep(12)

    while True:
        if exists('obj_1611823161695.jpg', timeOut=20, by=DriverType.CV):
            break
        else:
            sleep(12)
    sleep(4)

    try:
        # 进入游戏
        click('obj_1611720014683.jpg', position=(0.787, 0.86, 0.964, 0.944), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('进入游戏')
    sleep(4)

    if exists('obj_1611932170002.jpg', timeOut=20, by=DriverType.CV):
        try:
            click('obj_1611932188392.jpg', position=(0.93, 0.019, 0.954, 0.068), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:  
                click('obj_1611932215155.jpg', xOffset=0.824,yOffset=-0.89, position=(0.062, 0.901, 0.159, 0.966))
            except:    
                click((0.939, 0.049), position=None)
        sleep(12)

    if exists('obj_1612000297258.jpg', timeOut=20, by=DriverType.CV):
        try:
            click('obj_1612000282494.jpg', position=(0.87, 0.003, 0.908, 0.102), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click('obj_1612000312234.jpg', xOffset=0.109,yOffset=-0.398, position=(0.731, 0.368, 0.827, 0.539))
        sleep(4)

    while True:
        if exists('obj_1611827411445.jpg', timeOut=20, by=DriverType.CV):
            break
        else:
            sleep(12)
    
    try:
        # 立即前往
        click('obj_1611827411445.jpg', position=(0.668, 0.677, 0.848, 0.776), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
    except:
        click_text('立即前往')
    sleep(12)

    if exists('obj_1611932170002.jpg', timeOut=20, by=DriverType.CV):
        try:
            click('obj_1611932188392.jpg', position=(0.93, 0.019, 0.954, 0.068), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:  
                click('obj_1611932215155.jpg', xOffset=0.824,yOffset=-0.89, position=(0.062, 0.901, 0.159, 0.966))
            except:    
                click((0.939, 0.049), position=None)
        sleep(12)

    if exists('obj_1612000297258.jpg', timeOut=20, by=DriverType.CV):
        try:
            click('obj_1612000282494.jpg', position=(0.87, 0.003, 0.908, 0.102), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click('obj_1612000312234.jpg', xOffset=0.109,yOffset=-0.398, position=(0.731, 0.368, 0.827, 0.539))
        sleep(4)

    # 进入活动
    if exists('obj_1611827462336.jpg', timeOut=20, by=DriverType.CV):
        try:
            # A 物品1
            click('obj_1611827514796.jpg', position=(0.217, 0.372, 0.272, 0.473), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click((0.247, 0.42), position=None)
        sleep(3)

        try:
            # 关闭1
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # A物品2
            click('obj_1611827832467.jpg', position=(0.335, 0.381, 0.376, 0.467), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click((0.417, 0.416), position=None)
        sleep(3)

        try:
            # 关闭2
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # A物品3
            click('obj_1611887159185.jpg', position=(0.392, 0.372, 0.443, 0.483), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click((0.417, 0.416), position=None)
        sleep(3)

        try:
            # 关闭3
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # 进入B档
            click('obj_1611828370044.jpg', position=(0.345, 0.238, 0.413, 0.316), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611828407758.jpg', xOffset=-0.044,yOffset=0.088, position=(0.385, 0.158, 0.452, 0.211))
            except:
                pass
        sleep(3)

        try:
            # B物品1
            click('obj_1611887279055.jpg', position=(0.346, 0.235, 0.415, 0.322), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611887303988.jpg', xOffset=-0.043,yOffset=0.093, position=(0.386, 0.155, 0.452, 0.211))
            except:
                click((0.417, 0.416), position=None)
        sleep(3)

        try:
            # B物品1
            click('obj_1611892761916.jpg', position=(0.266, 0.368, 0.315, 0.477), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:   
                click('obj_1611892784487.jpg', xOffset=-0.13,yOffset=0.24, position=(0.383, 0.155, 0.455, 0.214))
            except:
                click((0.292, 0.436), position=None)
        sleep(3)

        try:
            # 关闭b1
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # B物品2
            click('obj_1611886638977.jpg', position=(0.323, 0.372, 0.381, 0.477), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611828528198.jpg', xOffset=-0.067,yOffset=0.226, position=(0.385, 0.155, 0.452, 0.223))
            except:
                click((0.417, 0.416), position=None)
        sleep(3)

        try:
            # 关闭b2
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # B物品3
            click('obj_1611828684851.jpg', position=(0.396, 0.384, 0.438, 0.471), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611828703437.jpg', xOffset=0,yOffset=0.238, position=(0.378, 0.155, 0.458, 0.211))
            except:
                click((0.417, 0.423), position=None)
        sleep(3)
    
        try:
            # 关闭b3
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # 进入C档
            click('obj_1611828743699.jpg', position=(0.419, 0.235, 0.489, 0.316), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611828763079.jpg', xOffset=0.039,yOffset=0.09, position=(0.382, 0.152, 0.449, 0.214))
            except:
                click((0.455, 0.269), position=None)
        sleep(3)
        
        try:
            # C物品1
            click('obj_1611828831596.jpg', position=(0.266, 0.378, 0.315, 0.48), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611828874033.jpg', xOffset=-0.129,yOffset=0.243, position=(0.383, 0.155, 0.452, 0.207))
            except:
                click((0.247, 0.42), position=None)
        sleep(3)

        try:
            # 关闭c1
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # C物品2
            click('obj_1611829015516.jpg', position=(0.33, 0.378, 0.378, 0.477), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try: 
                click('obj_1611829031897.jpg', xOffset=-0.064,yOffset=0.235, position=(0.383, 0.158, 0.452, 0.214))
            except:
                click((0.356, 0.416), position=None)
        sleep(3)

        try:
            # 关闭c2
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # C物品3
            click('obj_1611829076132.jpg', position=(0.393, 0.368, 0.443, 0.474), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611829093551.jpg', xOffset=-0.002,yOffset=0.234, position=(0.382, 0.152, 0.452, 0.211))
            except:
                click((0.42, 0.413), position=None)  
        sleep(3)
    
        try:
            # 关闭3
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

            #补充物品C
        try:
            click('obj_1611899944257.jpg', position=(0.268, 0.536, 0.315, 0.641), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click((0.289, 0.59), position=None)

        try:
            # 关闭bc
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # 切换D档
            click('obj_1611829173013.jpg', position=(0.501, 0.235, 0.564, 0.316), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611829192505.jpg', xOffset=0.114,yOffset=0.098, position=(0.375, 0.152, 0.456, 0.211))
            except:
                click((0.529, 0.272), position=None)
        sleep(3)
        
        try:
            # D物品1
            click('obj_1611900293816.jpg', position=(0.268, 0.372, 0.316, 0.474), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611829254032.jpg', xOffset=-0.127,yOffset=0.243, position=(0.382, 0.158, 0.454, 0.204))
            except:
                click((0.247, 0.42), position=None)
        sleep(3)

        try:
            # 关闭d1
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)
    
        try:
            # D物品2
            click('obj_1611829323566.jpg', position=(0.329, 0.365, 0.381, 0.486), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611829338512.jpg', xOffset=-0.067,yOffset=0.232, position=(0.379, 0.155, 0.458, 0.217))
            except:
                click((0.352, 0.407), position=None)
        sleep(3)

        try:
            # 关闭d2
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        try:
            # D物品3
            click('obj_1611829395466.jpg', position=(0.393, 0.372, 0.439, 0.474), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            try:
                click('obj_1611829411632.jpg', xOffset=-0.001,yOffset=0.24, position=(0.381, 0.155, 0.451, 0.214))
            except:
                click((0.42, 0.423), position=None)
        sleep(3)

        try:
            # 关闭d3
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

            #补充物品D
        try:   
            click('obj_1611900260984.jpg', position=(0.263, 0.533, 0.316, 0.641), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click((0.289, 0.59), position=None)
        try:
            # 关闭bc
            click('obj_1611887422679.jpg', position=(0.14, 0.084, 0.25, 0.706), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)            
        except:
            click((0.062, 0.452), position=None)
        sleep(3)

        if exists('obj_1611829471105.jpg', timeOut=20, by=DriverType.CV):
            try:
                # 确认奖池选择
                click('obj_1611829488526.jpg', position=(0.675, 0.712, 0.778, 0.78), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
            except:
                try:
                    click('obj_1611829517994.jpg', xOffset=-0.005,yOffset=0.557, position=(0.687, 0.149, 0.76, 0.211))
                except:
                    click_text('确认奖池选择')
            sleep(5)

        else:
            logger.info('奖励选择未满12个')

        sleep(5)

        try:
            # 确认奖池选择
            click('obj_1611829624038.jpg', position=(0.383, 0.675, 0.485, 0.749), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('确定')
        sleep(24)

        try:
            # 点击抽奖
            click('obj_1611829695413.jpg', position=(0.532, 0.74, 0.638, 0.811), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
        except:
            click_text('点击抽奖')
        sleep(12)

        if exists('obj_1611829779899.jpg', timeOut=20, by=DriverType.CV):
            try:
                click('obj_1611893161558.jpg', position=(0.382, 0.675, 0.486, 0.746), position_lock=0, animation=0, is_word=0, is_transparent=0, is_highlight=0)
            except:
                click_text('取消')
        sleep(24)
    else:
        logger.info('活动页未出现')
    pass