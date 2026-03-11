import { useContext, useState } from "react";
import { useNavigate} from 'react-router-dom'
import { AuthContext } from "../context/AuthContext";
import  api  from "../services/api";

function Login(){

    const navigate = useNavigate();
    const[username, setUsername] = useState("");
    const[password, setPassword] = useState("");
    const {setIsLoggedIn} = useContext(AuthContext)
    
    const handleLogin = async () => {
        const formData = new URLSearchParams();
        formData.append("username", username);
        formData.append("password", password);

        const res = api.post("/login",formData,{headers:{
            "Content-Type": "application/x-www-form-urlencoded"
        }})

        console.log(res)

        localStorage.setItem("token", res.access_token);
        localStorage.setItem("role",JSON.stringify(res.user));
        setIsLoggedIn(true);
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