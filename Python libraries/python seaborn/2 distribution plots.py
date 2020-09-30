import matplotlib.pyplot as plt
import seaborn as sns
data = sns.load_dataset("tips")
top = data.head(4)
print(top)
#dis_plot = sns.residplot(x="total_bill",y="tip",data = data,lowess=True)
#joint_plot = sns.jointplot(x="total_bill",y="tip",data=data,kind="kde")#kind="kde" changed plot from distribution to kde
# in joint_plot kde is different from kde line becuz kde line is 1 parameter and kde in joint_plot is 2 parameters
hex_plot = sns.jointplot(x="total_bill",y="tip",data=data,kind="hex",color="gold")# you should use hex, most ez one to see
#reg_plot = sns.jointplot(x="total_bill",y="tip",data=data,kind="reg",color="gold")
plt.show()
