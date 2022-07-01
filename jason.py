import pandas as pd

sample1=r"C:\Users\Debasish\Desktop\project\smp1.csv"
sample2=r"C:\Users\Debasish\Desktop\project\symbol.csv"

class Calculate:
    def __init__(self,Data):
        self.Data=Data
    def readcsv(self):
        df=pd.read_csv(self.Data)
        return df
    def addPL(self):
        df=self.readcsv()
        df["PL"]=round(df.Close-df.Open,2)
        df["PL_percent"]=round((df["PL"]/df.Open)*100,2)
        return df
    def addIndicator(self):
        df=self.addPL()
        indicator=[]
        for pl in df["PL"]:
            if pl > 0:
                indc="1"
            elif pl < 0:
                indc="0"
            else:
                indc=""
            indicator.append(indc)
        df["Indicator"]=indicator
        return df
    def percentprev(self):
        df=self.addIndicator()
        percent=[]
        for i in range(len(df)):
            profit_or_loss=df.Close[i]-df.Close[0]
            if (profit_or_loss ==0 ):
                per= 0
            else:
                per=(profit_or_loss/df.Close[0])*100 
     
            percent.append(round(per,2))

        
    
        df["Percent_prev"]=percent
        return df
    def show(self):
        df=self.percentprev()
        return df



class Stock_data:
    def __init__(self,DataFrame):
        self.DataFrame=DataFrame
        
    def Data(self):
        length=len(self.DataFrame)
        Dataset=[]
        for index in range(length):
            data={'Date':self.DataFrame.Date[index] , 'Open':self.DataFrame.Open[index] , 'High':self.DataFrame.High[index] , 'Low':self.DataFrame.Low[index] , 'Close':self.DataFrame.Close[index] , 'Volume':self.DataFrame.Volume[index] ,'PL':self.DataFrame["PL"][index],'PL_percent':self.DataFrame["PL_percent"][index] ,'Indicator':self.DataFrame["Indicator"][index],'Percent_prev':self.DataFrame["Percent_prev"][index]}
            Dataset.append(data)
        return Dataset
    def SymbolData(self):
        symbol_Dataset=[]
        length=len(self.DataFrame)
        for index in range(length):
            symbol_data={'Symbol':self.DataFrame.Symbol[index] , 'StockName':self.DataFrame.StockName[index]}
            symbol_Dataset.append(symbol_data)
        return symbol_Dataset



obj1=Calculate(sample1)
obj2=Calculate(sample2)

daataframe1=obj1.show()
daataframe2=obj2.readcsv()


obj_symbol=Stock_data(daataframe2)
object_Data=Stock_data(daataframe1)

object_Data.Data()
obj_symbol.SymbolData()