import { BrowserRouter, Route, Routes } from 'react-router-dom';

import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter basename="/">
        <Routes>
          <Route path="/summary" />
          <Route path="/" />
        </Routes>
        Home
      </BrowserRouter>
    </div>
  );
}

export default App;
