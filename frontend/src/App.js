import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState(null);

  const handleSubmit = async () => {
    const response = await axios.post('http://localhost:5000/predict', { features: [/* packet data */] });
    setData(response.data.prediction);
  };

  return (
    <div>
      <h1>Network Anomaly Detection</h1>
      <button onClick={handleSubmit}>Check Anomaly</button>
      {data && <p>Anomaly Status: {data}</p>}
    </div>
  );
}

export default App;
