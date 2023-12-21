import streamlit as st
from streamlit_charts import charts

st.set_page_config(page_title="streamlit-charts: Ant Design Charts for Streamlit!")

"""
# Welcome to [streamlit-charts](https://github.com/lxfu1/streamlit-charts)! 

[Ant Design Charts](https://github.com/ant-design/ant-design-charts) is AntV React component library, Simple and easy to use React chart library.
.

This project was created to allow us to render [Ant Design Charts](https://github.com/ant-design/ant-design-charts) in streamlit. In the meantime, below are some examples of what you can do with just a few lines of code:
"""

"""
## Column Chart
"""

options = {
    "data": [
        { "genre": "Sports", "sold": 275 },
        { "genre": "Strategy", "sold": 115 },
        { "genre": "Action", "sold": 120 },
        { "genre": "Shooter", "sold": 350 },
        { "genre": "Other", "sold": 150 },
    ],
    "xField": "genre",
    "yField": "sold",
    "colorField": "genre"
}

charts(type="Column", options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_charts import charts

options = {
    "data": [
        { "genre": "Sports", "sold": 275 },
        { "genre": "Strategy", "sold": 115 },
        { "genre": "Action", "sold": 120 },
        { "genre": "Shooter", "sold": 350 },
        { "genre": "Other", "sold": 150 },
    ],
    "xField": "genre",
    "yField": "sold",
    "colorField": "genre"
}

charts(type="Column", options=options)
```
""")



"""
## Bar Chart
"""

options = {
    "data": [
        { "genre": "Sports", "sold": 275 },
        { "genre": "Strategy", "sold": 115 },
        { "genre": "Action", "sold": 120 },
        { "genre": "Shooter", "sold": 350 },
        { "genre": "Other", "sold": 150 },
    ],
    "xField": "genre",
    "yField": "sold",
    "colorField": "genre"
}

charts(type="Bar", options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_charts import charts

options = {
    "data": [
        { "genre": "Sports", "sold": 275 },
        { "genre": "Strategy", "sold": 115 },
        { "genre": "Action", "sold": 120 },
        { "genre": "Shooter", "sold": 350 },
        { "genre": "Other", "sold": 150 },
    ],
    "xField": "genre",
    "yField": "sold",
    "colorField": "genre"
}

charts(type="Bar", options=options)
```
""")



"""
## Line Chart
"""

options = {
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/bmw-prod/551d80c6-a6be-4f3c-a82a-abd739e12977.csv",
    },
    "xField": "date",
    "yField": "close"
}

charts(type="Line", options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_charts import charts

options = {
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/bmw-prod/551d80c6-a6be-4f3c-a82a-abd739e12977.csv",
    },
    "xField": "date",
    "yField": "close"
}

charts(type="Line", options=options)
```
""")



"""
## Area Chart
"""

options = {
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/bmw-prod/551d80c6-a6be-4f3c-a82a-abd739e12977.csv",
    },
    "xField": "date",
    "yField": "close"
}

charts(type="Area", options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_charts import charts

options = {
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/bmw-prod/551d80c6-a6be-4f3c-a82a-abd739e12977.csv",
    },
    "xField": "date",
    "yField": "close"
}

charts(type="Area", options=options)
```
""")



"""
## Pie Chart
"""

options = {
    "data": [
        { "id": "c", "value": 526 },
        { "id": "sass", "value": 220 },
        { "id": "php", "value": 325 },
        { "id": "elixir", "value": 561 },
        { "id": "rust", "value": 54 }
    ],
    "colorField": "id",
    "angleField": "value",
    "style": {
        "radius": 4,
        "stroke": "#fff",
        "lineWidth": 1
    },
    "labels": [
        {
        "text": "value",
        "radius": 0.9
        }
    ],
    "animate": {
        "enter": {
        "type": "waveIn"
        }
    },
    "axis": False,
    "legend": False,
}

charts(type="Pie", options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_charts import charts

options = {
    "data": [
        { "id": "c", "value": 526 },
        { "id": "sass", "value": 220 },
        { "id": "php", "value": 325 },
        { "id": "elixir", "value": 561 },
        { "id": "rust", "value": 54 }
    ],
    "colorField": "id",
    "angleField": "value",
    "style": {
        "radius": 4,
        "stroke": "#fff",
        "lineWidth": 1
    },
    "labels": [
        {
        "text": "value",
        "radius": 0.9
        }
    ],
    "animate": {
        "enter": {
        "type": "waveIn"
        }
    },
    "axis": False,
    "legend": False,
}

charts(type="Pie", options=options)
```
""")



"""
## DualAxes Chart
"""

options = {
  "data": [
    {
      "Month": "Jan",
      "Evaporation": 2,
      "Precipitation": 2.6,
      "Temperature": 2
    },
    {
      "Month": "Feb",
      "Evaporation": 4.9,
      "Precipitation": 5.9,
      "Temperature": 2.2
    },
    {
      "Month": "Mar",
      "Evaporation": 7,
      "Precipitation": 9,
      "Temperature": 3.3
    },
    {
      "Month": "Apr",
      "Evaporation": 23.2,
      "Precipitation": 26.4,
      "Temperature": 4.5
    },
    {
      "Month": "May",
      "Evaporation": 25.6,
      "Precipitation": 28.7,
      "Temperature": 6.3
    },
    {
      "Month": "Jun",
      "Evaporation": 76.7,
      "Precipitation": 70.7,
      "Temperature": 10.2
    },
    {
      "Month": "Jul",
      "Evaporation": 135.6,
      "Precipitation": 175.6,
      "Temperature": 20.3
    },
    {
      "Month": "Aug",
      "Evaporation": 162.2,
      "Precipitation": 182.2,
      "Temperature": 23.4
    },
    {
      "Month": "Sep",
      "Evaporation": 32.6,
      "Precipitation": 48.7,
      "Temperature": 23
    },
    {
      "Month": "Oct",
      "Evaporation": 20,
      "Precipitation": 18.8,
      "Temperature": 16.5
    },
    {
      "Month": "Nov",
      "Evaporation": 6.4,
      "Precipitation": 6,
      "Temperature": 12
    },
    {
      "Month": "Dec",
      "Evaporation": 3.3,
      "Precipitation": 2.3,
      "Temperature": 6.2
    }
  ],
  "xField": "Month",
  "children": [
    {
      "type": "line",
      "yField": "Temperature",
      "colorField": "#EE6666",
      "shapeField": "smooth",
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 30
        }
      },
      "axis": {
        "y": {
          "title": "Temperature (°C)",
          "grid": None,
          "titleFill": "#EE6666"
        }
      }
    },
    {
      "type": "interval",
      "yField": "Evaporation",
      "colorField": "#5470C6",
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 200
        }
      },
      "style": {
        "fillOpacity": 0.8
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Evaporation (ml)",
          "titleFill": "#5470C6"
        }
      }
    },
    {
      "type": "line",
      "yField": "Precipitation",
      "colorField": "#91CC75",
      "scale": {
        "y": {
          "independent": True
        }
      },
      "style": {
        "lineWidth": 2,
        "lineDash": [
          2,
          2
        ]
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Precipitation (ml)",
          "grid": None,
          "titleFill": "#91CC75"
        }
      }
    }
  ]
}

charts(type="DualAxes", options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_charts import charts

options = {
  "data": [
    {
      "Month": "Jan",
      "Evaporation": 2,
      "Precipitation": 2.6,
      "Temperature": 2
    },
    {
      "Month": "Feb",
      "Evaporation": 4.9,
      "Precipitation": 5.9,
      "Temperature": 2.2
    },
    {
      "Month": "Mar",
      "Evaporation": 7,
      "Precipitation": 9,
      "Temperature": 3.3
    },
    {
      "Month": "Apr",
      "Evaporation": 23.2,
      "Precipitation": 26.4,
      "Temperature": 4.5
    },
    {
      "Month": "May",
      "Evaporation": 25.6,
      "Precipitation": 28.7,
      "Temperature": 6.3
    },
    {
      "Month": "Jun",
      "Evaporation": 76.7,
      "Precipitation": 70.7,
      "Temperature": 10.2
    },
    {
      "Month": "Jul",
      "Evaporation": 135.6,
      "Precipitation": 175.6,
      "Temperature": 20.3
    },
    {
      "Month": "Aug",
      "Evaporation": 162.2,
      "Precipitation": 182.2,
      "Temperature": 23.4
    },
    {
      "Month": "Sep",
      "Evaporation": 32.6,
      "Precipitation": 48.7,
      "Temperature": 23
    },
    {
      "Month": "Oct",
      "Evaporation": 20,
      "Precipitation": 18.8,
      "Temperature": 16.5
    },
    {
      "Month": "Nov",
      "Evaporation": 6.4,
      "Precipitation": 6,
      "Temperature": 12
    },
    {
      "Month": "Dec",
      "Evaporation": 3.3,
      "Precipitation": 2.3,
      "Temperature": 6.2
    }
  ],
  "xField": "Month",
  "children": [
    {
      "type": "line",
      "yField": "Temperature",
      "colorField": "#EE6666",
      "shapeField": "smooth",
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 30
        }
      },
      "axis": {
        "y": {
          "title": "Temperature (°C)",
          "grid": None,
          "titleFill": "#EE6666"
        }
      }
    },
    {
      "type": "interval",
      "yField": "Evaporation",
      "colorField": "#5470C6",
      "scale": {
        "y": {
          "independent": True,
          "domainMax": 200
        }
      },
      "style": {
        "fillOpacity": 0.8
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Evaporation (ml)",
          "titleFill": "#5470C6"
        }
      }
    },
    {
      "type": "line",
      "yField": "Precipitation",
      "colorField": "#91CC75",
      "scale": {
        "y": {
          "independent": True
        }
      },
      "style": {
        "lineWidth": 2,
        "lineDash": [
          2,
          2
        ]
      },
      "axis": {
        "y": {
          "position": "right",
          "title": "Precipitation (ml)",
          "grid": None,
          "titleFill": "#91CC75"
        }
      }
    }
  ]
}

charts(type="DualAxes", options=options)
```
""")


"""
## Scatter Chart
"""

options = {
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/basement_prod/6b4aa721-b039-49b9-99d8-540b3f87d339.json",
    },
    "xField": "height",
    "yField": "weight",
    "colorField": "gender",
    "shapeField": "point"
}

charts(type="Scatter", options=options)

source = st.expander("Source Code")
source.markdown("""
```py
import streamlit as st
from streamlit_charts import charts

options = {
    "data": {
        "type": "fetch",
        "value": "https://gw.alipayobjects.com/os/basement_prod/6b4aa721-b039-49b9-99d8-540b3f87d339.json",
    },
    "xField": "height",
    "yField": "weight",
    "colorField": "gender",
    "shapeField": "point"
}

charts(type="Scatter", options=options)
```
""")
