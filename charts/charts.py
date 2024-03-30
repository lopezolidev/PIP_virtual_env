import matplotlib.pyplot as plt

def generate_pie_chart():
    values = [200 , 120, 300]
    labels = ['A', 'B', 'C']
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()

