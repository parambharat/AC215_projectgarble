import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Home from './Pages/Home';
import Summary from './Pages/Summary';

import Theme from './Theme';
import {
  ThemeProvider,
} from '@mui/material/styles';


function App() {
  return (
    <div className="App">
      <ThemeProvider theme={Theme}>
        <BrowserRouter basename="/">
          <Routes>
            <Route path="/summary" element={<Summary />} />
            <Route path="/" element={<Home />} />
          </Routes>
        </BrowserRouter>
      </ThemeProvider>
    </div>
  );
}

export default App;
