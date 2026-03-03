import { Link } from "react-router-dom"

function Navbar() {
    const token = localStorage.getItem("token");

    return(
        <nav>
            <Link to="/" >Home</Link>

            {!token && (
                <>
                    < Link to="/signup">Signup</Link>
                    < Link to="/login">Login</Link>
                </>
            )}

            {token && (
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