function Admin() {

    const token = localStorage.getItem("token")

    if(!token){
        return <h2>Not Authorized my man</h2>
    }
    return (<h2>Authorized</h2>)
}

export default Admin