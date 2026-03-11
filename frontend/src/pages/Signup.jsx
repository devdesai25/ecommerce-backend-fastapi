import { useState } from "react";
import api from "../services/api";

function Signup(){
   
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async() => {

        const res = await api.post(
            "/signup",
            JSON.stringify({
                username : username,
                password: password
            })
        );
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