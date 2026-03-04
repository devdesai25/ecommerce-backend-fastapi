import { useState, useEffect } from 'react'
import { BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/Home'
import Signup from './pages/Signup'
import Login from './pages/Login'
import Admin from './pages/Admin'
import Navbar from './components/Navbar'
import axios from "axios"

function App() {
  const [message, setMessage] = useState("")
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem("token"));

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/")
    .then(res => setMessage(res.data.message))
    .catch(err => console.log(err));
  },[]);

  return (
    <BrowserRouter>
    <Navbar isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/login' element={<Login setIsLoggedIn={setIsLoggedIn} />} />
        <Route path='/signup' element={<Signup />} />
        <Route path='/Admin' element={<Admin />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App