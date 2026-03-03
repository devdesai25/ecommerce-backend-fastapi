import { useState, useEffect } from "react"

function Home(){
    
    const [products, setProduct] = useState([])

    useEffect(()=>{
        const fetchProducts = async () => {
        try{    const res = await fetch("http://localhost:8000/products");
            const data = await res.json();
            setProduct(data);
        }catch(error){
            console.log("Error fetching products",error)
        }
    };
    fetchProducts()

}, []);
    
    return (<div>
        {products.map( product =>(
            <div>
                <h3>{product.name}</h3>
                <h3>{product.price}</h3>
                <h3>{product.description}</h3>
                <br></br>
                <br></br>
            </div>
        ))}
    </div>)
}

export default Home