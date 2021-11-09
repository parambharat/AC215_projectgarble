import { BrowserRouter, Route, Routes } from 'react-router-dom';

import './App.css';

import Home from './Pages/Home';
import Summary from './Pages/Summary';


function App() {
  return (
    <div className="App">
      <BrowserRouter basename="/">
        <Routes>
          <Route path="/summary" element={<Summary/>}/>
          <Route path="/" element={<Home/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
