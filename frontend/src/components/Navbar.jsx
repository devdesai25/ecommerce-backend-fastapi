import { Link } from "react-router-dom"

function Navbar({isLoggedIn, setIsLoggedIn}) {

    const token = localStorage.getItem("token");
    
    console.log("Navbar render", isLoggedIn)
    return(
        <nav>
            <Link to="/" >Home</Link>

            {isLoggedIn && (
                <>
                    < Link to="/admin">Admin</Link>
                    
                    < button onClick={() => {
                        localStorage.removeItem("token");
                        setIsLoggedIn(false);
                        //window.location.reload();
                    }}>
                        Logout
                    </button>
                </>
            )}

            {!isLoggedIn && (
                <>
                    < Link to="/signup">Signup</Link>
                    < Link to="/login">Login</Link>
                </>
            )}

        </nav>
    )
}

export default Navbar