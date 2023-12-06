import axios from "axios";
import React, { useEffect, useRef, useState } from "react";
import { useNavigate } from "react-router";

export function Dash() {
    let [data, setdata ]= useState([])
    let [ l, sl ] = useState(false)
    let tref=useRef()
    let dref=useRef()
    let pref=useRef()
    let [toggle,setoggle]=useState(true)
     const nav=useNavigate()
    useEffect(() => {
        axios.post(`http://127.0.0.1:80/api/data/view/${sessionStorage.getItem('name')}`)
        .then((r)=>{
            console.log(r.data)
            setdata(r.data)
            sl(true)
        })

    }, [toggle])
    function submit(){
        console.log(tref.current.value,pref.current.value,dref.current.value)
        let d={
            'title':tref.current.value,
            'desc':dref.current.value,
            'priority':pref.current.value,
            'user':sessionStorage.getItem('name')
        }
        axios.post('http://127.0.0.1:80/api/data/create',d)
        .then((r)=>{
            if(r.status=202){
                alert('task created')
                setoggle(!toggle)

            }
            else{
                alert('could not create')

            }
        })
    }
    function logout(){
        sessionStorage.removeItem('name')
        nav('/')
        
    }
    function deltask(e){
        console.log(e.target.getAttribute('data'))
        axios.delete(`http://127.0.0.1:80/api/data/delete/${e.target.getAttribute('data')}`)
        .then((r)=>{
            if(r.status==202){
                alert('task deleted')
                setoggle(!toggle)
            }
            else{
                alert('issue while deleting task')
            }
        })

    }
    return (
        <div className="hcont">
            <div className="ct">
                <label htmlFor="">
                    Title
                    <input ref={tref} type="text" />
                </label>
                <label htmlFor="">
                    Description
                    <textarea ref={dref} name="gg" id="1" cols="40" rows="5"></textarea>
                </label>
                <label htmlFor="">
                    Priority
                    <select name="" id="" ref={pref}>
                        <option value="high">high</option>
                        <option value="med">Med</option>
                        <option value="low">Low</option>
                    </select>
                </label>
                <button onClick={submit}>create task</button>
            </div>
            <div className="task_list">

                {l && data.map((e) => {
                    return (
                        <div key={e.id} className="task">
                            <p>{e.title}</p>
                            <p>{e.desc}</p>
                            <p>{e.priority}</p>
                            <button onClick={deltask} data={e.id}>delete</button>
                        </div>
                    )
                })}

            </div>
            <button onClick={logout}>Logout</button>
        </div>
    )
}