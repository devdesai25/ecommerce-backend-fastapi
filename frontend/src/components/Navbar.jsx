import { Link } from "react-router-dom"

function Navbar({isLoggedIn, setIsLoggedIn}) {
    const token = localStorage.getItem("token");

    return(
        <nav>
            <Link to="/" >Home</Link>

            {!isLoggedIn && (
                <>
                    < Link to="/signup">Signup</Link>
                    < Link to="/login">Login</Link>
                </>
            )}

            {isLoggedIn && (
                <>
                    < Link to="/admin">Admin</Link>
                    
                    < button onClick={() => {
                        localStorage.removeItem("token");
                        window.location.reload();
                    }}>
                        Logout
                    </button>
                </>
            )}
        </nav>
    )
}

export default Navbar