import { useState, useEffect } from "react"
import "./Home.css"
import api from "../services/api";

function Home(){
    
    const [products, setProduct] = useState([])

    const fetchProducts = async () => {
        try{
            const res = await api.get("/products")    
            setProduct(res.data);
        }catch(error){
            console.log("Error fetching products",error)
        }
    };

    useEffect(()=>{
    
        fetchProducts()

    }, []);
    
    return (<div className="product-grid">
        {products.map(product => (
            <div key={product.product_id} className="card">
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