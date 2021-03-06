import plotly.graph_objects as go

'''
    Utilities to generate charts on the changes of the fitness through generations
'''
def create_figure():
  return go.Figure()
  
def plot_figure(fig, chart_data, title, x_title, y_title):  

  for dataset in chart_data:
    y_axis = [float(x) for x in dataset['y_data']]
    fig.add_scatter(
      y=y_axis,
      x=[x+1 for x in range(len(y_axis))],
      mode="lines+markers", 
      textposition="bottom center",
      name=dataset['label'],
      line={"color": dataset['color'], "width": 1}
    )

  fig.update_layout(
    title=title,
    width=1024,
    height=400,
    xaxis={"title": x_title},
    yaxis={"title": y_title, "tickformat": ".2f"},
    font=dict(
      family="Courier New, monospace",
      size=14,
      color="#7f7f7f"
    )
  )

# Example input data
# labels = ['Elem1', 'Elem2', 'Elem3', 'Elem4']
# data_x =  ['Elemen1', 'Elemen2', 'Elemen3', 'Elemen4']
# data_y = [[3,8,9,5],[2,4,8,6],[1,8,9,2],[3,4,6,7]]
# titles = {'title':'Titulo global', 'x_title': 'clases', 'y_title': 'valores'}
def plot_multiBar(fig, labels, data_x, data_y, titles):
  plot_data = []
  for i in range(len(labels)):
    plot_data.append( go.Bar(name=labels[i], x=data_x, y=data_y[i]) )
  fig.add_traces(data=plot_data)
  
  fig.update_layout(
    width=1024,
    height=400,
    title=titles['title'],
    xaxis={"title": titles['x_title']},
    yaxis={"title": titles['y_title'], "tickformat": ".2f"},
    barmode='group',
    font=dict(
      family="Courier New, monospace",
      size=14,
      color="#7f7f7f"
    )
  )