import numpy as np

class Knapsack:
    def __init__(self,p,w,M,n):
        self.n = n
        self.M = M
        self.p, self.w = self.density(p, w) 

    def density(self,p,w):
        dens = []
        for i in range(len(p)):
            dens.append(p[i]/w[i])

        p_densed = []
        w_densed = []
        for j in range(len(dens)):
            maks = max(dens)
            i_maks = dens.index(maks)
            p_densed.append(p[i_maks])
            w_densed.append(w[i_maks])
            dens[i_maks] = 0
            
        return p_densed, w_densed
    
    def start(self):
        #untuk menampung semua x1,x2,...,xn
        x = []
        for i in range(self.n):
            x.append(0)
        isi = self.M
        
        i = 1
        for i in range(self.n):
            if self.w[i] > isi:
                break
            else:
                x[i] = 1
                isi = isi - self.w[i]
        if i <= self.n :
            x[i] = isi / self.w[i]
            
        return x
    
    def findTujuan(self,x):
        p_x = []
        for i in range(len(self.p)):
            p_x.append(self.p[i] * x[i])
        sum_p_x = sum(p_x)
        return sum_p_x
        

if __name__ == "__main__":
    title = "Program by prokoding"
    print(title.center(50,'*'))
    try:
        n = int(input('Masukan banyak data : '))
        if n < 0:
            print('Some Error Detected')
        else:
            p =[]
            w = []
            for i in range(n):
                px = int(input('Masukan p'+str(i+1)+' '))
                p.append(px)
            print('============')
            for j in range(n):
                wx = int(input('Masukan w'+str(j+1)+' '))
                w.append(wx)
            M = int(input('Masukan total banyak : '))
            clf = Knapsack(np.array(p),np.array(w),M,n)
            x_value = clf.start()
            print('Nilai x dalam kasus tersebut : ',x_value)
            f_tujuan = clf.findTujuan(x_value)
            print('Nilai fungsi tujuan : ',f_tujuan)
        
    except Exception as e:
        print('Algoritma Not Working')




















    
