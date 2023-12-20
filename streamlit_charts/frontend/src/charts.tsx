import React from "react"
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"
import * as AntDesignCharts from "@ant-design/charts"

const ChartsComponent: React.FC<ComponentProps> = (props) => {
  const { type = "Column", options } = props.args
  const { onReady, ...rest } = options
  const Component = (AntDesignCharts as any)[type]

  if (!Component) {
    return <div>Invalid type: {type}</div>
  }

  return (
    <Component
      onReady={(...args: any[]) => {
        Streamlit.setFrameHeight()
        onReady?.(...args)
      }}
      {...rest}
    />
  )
}

export const Charts = withStreamlitConnection(ChartsComponent)
