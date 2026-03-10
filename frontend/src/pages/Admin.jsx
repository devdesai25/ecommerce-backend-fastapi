import { useState } from "react"

function Admin() {

//    if(!token){
//        return <h2>Not Authorized my man</h2>
//    }
//    return (<h2>Authorized</h2>)

//    const user = JSON.stringify(localStorage.getItem("user"))
//    if(user.role!=="admin"){
//        return (<div>
//            <h2>Not Authorized</h2>
//        </div>)
//    }


    const [name, setName] = useState("");
    const [price, setPrice] = useState("");
    const [description, setDescription] = useState("");
    const [stock, setStock] = useState("");
    const [deleteId, setDeleteId] = useState("");
    const [updateId, setUpdateId] = useState("");

        const handleCreate = async () => {

            const token = localStorage.getItem("token")

            
            await fetch("http://localhost:8000/admin/create",{
                method : "POST",

                headers : {
                    "Content-Type" : "application/json",
                    "Authorization": `Bearer ${token}`
                },
                body : JSON.stringify({
                    name,
                    price : Number(price),
                    description,
                    stock : Number(stock)
                })
            });

        };    

        const handleDelete = async () => {

            const token = localStorage.getItem("token")

            await fetch(`http://localhost:8000/admin/delete/${deleteId}`,{
                
                method: "DELETE",

                headers : {
                    "Authorization" : `Bearer ${token}`
                }
            });
        };

        const handleUpdate = async () => {
 
            const token = localStorage.getItem("token")

            const updateData = {}

            if(name) updateData.name = name
            if(description) updateData.description = description
            if(price) updateData.price = Number(price)
            if(stock) updateData.stock = Number(stock)


            await fetch(`http://localhost:8000/admin/update/${updateId}`,{

                method : "PATCH",

                headers : {
                    "Authorization" : `Bearer ${token}`,
                    "Content-Type" : "application/json" 
                },
                body : JSON.stringify(updateData)
            })
        };


    return (
        <div>
            <div className="input">

                <h2>Input</h2>
                
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
            
            <div className="delete">
                <h2>Delete</h2>
                <input 
                placeholder="DeleteId"
                value = {deleteId}
                onChange = {(e)=>setDeleteId(e.target.value)}
                />

                <button onClick={handleDelete}>
                    Delete
                </button>
            </div>
            <div className="update">
                
                <h2>Update</h2>

                <input 
                placeholder="Enter Update Id"
                value = {updateId}
                onChange = {(e)=>setUpdateId(e.target.value)}
                />

                <input 
                placeholder = "Enter New Name"
                value = {name}
                onChange = {(e)=>setName(e.target.value)}
                />

                <input 
                placeholder = "Enter New Description"
                value = {description}
                onChange = {(e)=>setDescription(e.target.value)}
                />

                <input 
                placeholder= "Enter New Price"
                value = {price}
                onChange = {(e)=>setPrice(e.target.value)}
                />

                <input 
                placeholder = "Enter New Stock"
                value = {stock}
                onChange = {(e)=>setStock(e.target.value)}
                />

                <button onClick={handleUpdate}>
                    Update
                </button>

            </div>
            
        </div>
    )
};
export default Admin