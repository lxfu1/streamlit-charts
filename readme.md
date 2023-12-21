<h1 align="center">
  <b>Streamlit Charts</b>
</h1>

<div align="center">

[Ant Design Charts](https://ant-design-charts.antgroup.com/) is AntV React component library, Simple and easy to use React chart library.

This project was created to allow us to render [Ant Design Charts](https://github.com/ant-design/ant-design-charts) charts in streamlit.

![examples](https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*11uNQrnKdFoAAAAAAAAAAAAADmJ7AQ/original)
![Build Status](https://github.com/ant-design/ant-design-charts/workflows/build/badge.svg)
![npm Version](https://img.shields.io/npm/v/@ant-design/charts)
![npm Download](https://img.shields.io/npm/dm/@ant-design/charts)
[![GitHub stars](https://img.shields.io/github/stars/ant-design/ant-design-charts)](https://github.com/ant-design/ant-design-charts/stargazers)
[![npm License](https://img.shields.io/npm/l/@ant-design/charts.svg)](https://www.npmjs.com/package/@ant-design/charts)

</div>


## Installation

```
pip3 install streamlit-charts 
```


## Usage

```py
import streamlit as st
from streamlit_charts import charts

 options = {
    "height": 400,
    "data": [
        { "genre": "Sports", "sold": 275 },
        { "genre": "Strategy", "sold": 115 },
        { "genre": "Action", "sold": 120 },
        { "genre": "Shooter", "sold": 350 },
        { "genre": "Other", "sold": 150 },
    ],
    "xField": 'genre',
    "yField": 'sold',
    "colorField": "genre",
    "style": {
      "radiusTopLeft": 10,
      "radiusTopRight": 10,
    },
  }

  charts(options=options, type="Column", key="streamlit-charts")
```

<img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*aPxqSpQcsUQAAAAAAAAAAAAADmJ7AQ/original" width="640" alt="example">


## API

Now, There is only one API for `streamlit-charts`, named `charts`, see the `options` in [Ant Design Charts](https://ant-design-charts.antgroup.com/).

| Property | Description                                                                                                     | Type                  | Default |
| -------- | --------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| options  | the [options](https://ant-design-charts.antgroup.com/) for the visualization | `Options` \| `null` | -       |
| type    | the chart type of the charts                                                                                      | `Str`       | `Column`      |


## Development

- Building frontend code by running `npm run start` in fold `streamlit_charts/frontend`.
- Run the example by running `streamlit run streamlit_charts/__init__.py` with `_RELEASE = False`.


## License

MIT@[lxfu1](https://github.com/lxfu1).
