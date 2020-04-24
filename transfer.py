
class TemperatureTrans:#温度单位转换类
    def FahrenheitToCelsius(self,f): #华氏温度到摄氏温度转换方法
        c=round((f+(-32))/1.8,1) 
        return c
    def CelsiusToFahrenheit(self,c): #摄氏温度到华氏温度转换方法
        f=c*1.8+32
        return f

class LengthTrans:#长度单位转换类
    def inchToCent(self,inch):#英寸到厘米转换方法
        cent=round(inch/0.3937,2)
        return cent
    def centToInch(self,cent):#厘米到英寸转换方法
        inch=0.3937*cent
        return inch

class CurrencyTrans:#货币单位转换类
    def dollarToRMB(self,d):#美元到人民币转换方法
        r=7.062*d
        return r
    def RMBToDollar(self,r):#人民币到没有转换方法
        d=0.1416*r 
        return d


class Transfer:#主程序类
    def transfer(self):#主程序方法，控制输入输出
        while True:
            unitType=input('请输入单位转换类型：\n1.温度单位转换（华氏温度与摄氏温度）\n2.长度单位转换（中国与美国长度单位）\n3.货币单位转换（美元与人民币）\n按任意键取消\n')
            if unitType=='1':
                temper=TemperatureTrans()
                while True:
                    typeBfConvert=input('请输入需要转换的温度类型：\n1.摄氏温度\n2.华氏温度\n3.按任意键取消\n')
                    if typeBfConvert=='1':
                        try:
                            c=float(input('请输入摄氏温度值：\n'))
                            f=temper.CelsiusToFahrenheit(c)
                            print(f'摄氏温度{c}对应的华氏温度为：{f}\n-------')
                        except:
                            print('输入错误，请重新输入！')
                    elif typeBfConvert=='2':
                        try:
                            f=float(input('请输入华氏温度值：\n'))
                            c=temper.FahrenheitToCelsius(f)
                            print(f'华氏温度{f}对应的摄氏温度为：{c}\n-------')
                        except:
                            print('输入错误，请重新输入！')
                    else:
                        break   
            elif unitType=='2':
                len=LengthTrans()
                while True:
                    typeBfConvert=input('请输入需要转换的长度类型：\n1.中国\n2.美国\n3.按任意键取消\n')
                    if typeBfConvert=='1':
                        try:
                            cent=float(input('请输入中国长度值（厘米）：\n'))
                            inch=len.centToInch(cent)
                            print(f'{cent}厘米对应{inch}英寸\n-------\n')
                        except:
                            print("输入错误，请重新输入！")
                    elif typeBfConvert=='2':
                        try:
                            inch=float(input('请输入美国长度值（英寸）：\n'))
                            cent=len.inchToCent(inch)
                            print(f'{inch}英寸对应{cent}厘米\n-------\n')
                        except:
                            print("输入错误，请重新输入！")
                    else:
                        break
            elif unitType=='3':
                cur=CurrencyTrans()
                while True:
                    typeBfConvert=input('请输入需要转换的货币类型：\n1.人民币\n2.美元\n3.按任意键取消\n')
                    if typeBfConvert=='1':
                        try:
                            r=float(input('请输入人民币值（元）：\n'))
                            d=cur.RMBToDollar(r)
                            print(f'{r}人民币对应{d}美元\n-------\n')
                        except:
                            print("输入错误，请重新输入！")
                    elif typeBfConvert=='2':
                        try:
                            d=float(input('请输入美元值（美元）：\n'))
                            r=cur.dollarToRMB(d)
                            print(f'{d}美元对应{r}人民币\n-------\n')
                        except:
                            print("输入错误，请重新输入！")
                    else:
                        break
            else:
                break

if __name__=="__main__":#程序入口
    trans=Transfer() 
    trans.transfer()   

    


  