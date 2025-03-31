import {useState} from 'react'
import Dashboard from './Dashboard'

const App = () => {
  const [count, setCount] = useState(0)
  const handleIncrementByTen = () => {
    setCount(count + 10)
  }

  const handleDecrementByTen = () => {
    setCount(count - 10)
  }

  const resetCountHandler = () => {
    setCount(0)
  }

  return (
    // Layout
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', padding: '1rem' }}>
      
      {/* start box frame */}
      <div>
        <h2>Counter</h2>
        <div>
          Initial Count: {count}
        </div>  
        <hr />
    
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          
          <button type="button" onClick={handleIncrementByTen}>
            Increment by 10
          </button>
      
          <button type="button" onClick={handleDecrementByTen}>
            Decrement by 10
          </button>
      
          <button type="button" onClick={resetCountHandler}>
            Reset Count
          </button>
        </div>
      </div>
      {/* end of box frame */}

      <div>
        <h2>Dashboard</h2>
        <Dashboard />
      </div>

    {/* End of Layout */}
    </div> 

  )

}

export default App;
