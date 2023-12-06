import React from "react";
import  ReactDOM  from "react-dom/client";
import  {BrowserRouter,Route,Routes} from "react-router-dom"
import {Home} from "./components/Home.jsx"
import { Dash } from "./components/dash.jsx";
import './styles/main.css'
const root=ReactDOM.createRoot(document.getElementById('root'))
root.render(
    <BrowserRouter>
    <Routes>
        <Route path="/*" element={<Home/>}/>
        <Route path="dash" element={<Dash/>}/>

    </Routes>
    
    </BrowserRouter>

)