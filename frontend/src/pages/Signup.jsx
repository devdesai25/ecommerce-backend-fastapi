import { useState } from "react";

function Signup(){
   
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async() => {

        const res = await fetch("http://localhost:8000/signup",{
            method : "POST",
            headers : {
                "Content-Type" : "application/json",
            },
            body : JSON.stringify({
                username : username,
                password : password
            })

        });

        const data = await res.json()

        console.log(data)
    }
    
    return (<div>
        <input 
        placeholder="Username"
        value = {username}
        onChange = {(e)=>setUsername(e.target.value)}
        />

        <input 
        placeholder="Password"
        value = {password}
        onChange = {(e)=>setPassword(e.target.value)}
        />

        <button onClick={ handleSubmit}>Submit</button>

    </div>)
}

export default Signup;