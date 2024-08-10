import { useState } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom';

//imported component
import Component1 from './components/component1';
import Component2 from './components/component2';



function App() {
  
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Component1></Component1>}></Route>
        <Route path="/component2" element={<Component2></Component2>}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App
