import { useState, useEffect } from "react"
import "./Home.css"
function Home(){
    
    const [products, setProduct] = useState([])

    const fetchProducts = async () => {
        try{    
            const res = await fetch("http://localhost:8000/products");
            const data = await res.json();
            setProduct(data);
        }catch(error){
            console.log("Error fetching products",error)
        }
    };

    useEffect(()=>{
    
        fetchProducts()

    }, []);
    
    return (<div className="product-grid">
        {products.map( product =>(
            <div className="card" key={product.id}>
                <h3>{product.name}</h3>
                <p className="price">
                {product.price}
                </p>
                <p className="description">
                {product.description}
                </p>
            </div>
        ))}
    </div>)
}

export default Home