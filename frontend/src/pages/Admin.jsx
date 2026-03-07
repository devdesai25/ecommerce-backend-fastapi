import { use, useState } from "react"

function Admin() {

//    if(!token){
//        return <h2>Not Authorized my man</h2>
//    }
//    return (<h2>Authorized</h2>)

    const user = JSON.stringify(localStorage.getItem("user"))
    if(user.role!=="admin"){
        return (<div>
            <h2>Not Authorized</h2>
        </div>)
    }


    const [name, setName] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");
    const [stock, setStock] = useState("");

    const handleCreate = async () => {

        const token = localStorage.getItem("token")

        
        await fetch("http://localhost:8000/admin/create",{
            method : "POST",

            headers : {
                "Content-Type" : "application:json",
                "Authorization-Token": `Bearer ${token}`
            },
            body : JSON.stringify({
                name,
                price : Number(price),
                description,
                stock : Number(stock)
            })
        });

    };

    return (
        <div>
            <input 
            placeholder="Name"
            value = {name}
            onChange = {(e)=>setName(e.target.value)}
            />

            <input 
            placeholder="Price"
            value = {price}
            onChange = {(e)=>setPrice(e.target.value)}
            />

            <input 
            placeholder="Description"
            value= {description}
            onChange = {(e)=>setDescription(e.target.value)}
            />

            <input 
            placeholder="Stock"
            value= {stock}
            onChange = {(e)=>setStock(e.target.value)}
            />

            <button onClick={handleCreate}>Create Product</button>
        </div>
    )

}

export default Admin