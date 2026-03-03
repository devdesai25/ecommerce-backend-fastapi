import { useState } from "react";
import { useNavigate} from 'react-router-dom'

function Login(){

    const navigate = useNavigate();
    const[username, setUsername] = useState("");
    const[password, setPassword] = useState("");

    const handleLogin = async () => {
        const formData = new URLSearchParams();
        formData.append("username", username);
        formData.append("password", password);

        const res = await fetch("http://localhost:8000/login",{
            method : "POST",
            headers : {
                "Content-Type" : "application/x-www-form-urlencoded",
            },
            body : formData
        });

        const data = await res.json()
        console.log(data)

        localStorage.setItem("token", data.access_token);
        navigate("/");

    };

    return(
    <div>
        <input 
        placeholder = "Username"
        value = {username}
        onChange = {(e) => setUsername(e.target.value)}
        />

        <input 
        placeholder = "Password"
        value = {password}
        onChange = {(e) => setPassword(e.target.value)}
        />

        <button onClick={handleLogin}>Login</button>
    </div>
    
    )
}

export default Login;