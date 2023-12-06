import React, { useEffect, useRef } from "react";
import {useNavigate} from "react-router"
import axios from "axios";
export function Home(){
    const uref=useRef()
    const pref=useRef()
    const nav=useNavigate()
    
    function login(){
        let data={
            name:uref.current.value,
            pass:pref.current.value,
        }
        axios.post('http://127.0.0.1/api/login/verify',data)
        .then((r)=>{
            if(r.status==202){
                alert('logged in')
                sessionStorage.setItem('name',data.name)
                nav('dash')
            }
            else{
                alert('wrong uname or pass')
            }
        })
    }
    function reg(){
        let data={
            name:uref.current.value,
            pass:pref.current.value,
        }
        axios.post('http://127.0.0.1:80/api/login/reg',data)
        .then((r)=>{

            if(r.status!=201){
                alert('correct name and pass')
            }
            else{
                alert('username created')
            }
        }
        )
    }

    return(
        <div className="hcont">

        <div className="home">
            <label htmlFor="">
            Username
            <input type="text" ref={uref} />
            </label>
            <label htmlFor="">

            Passsword
            <input type="password" ref={pref} />
            </label>
            <div>
                <button onClick={login}>Login</button>
                <button onClick={reg}>Register</button>
            </div>
        </div>
        </div>
    )
}