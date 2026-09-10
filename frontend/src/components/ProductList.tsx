import Product, { ProductProps } from "./Product";

export interface ProductListProps {
    products: ProductProps[];
}


export default function ProductList({ products }: ProductListProps) {
    return (
        <div className="flex">
            {products.map(product => (
               (
                <Product key={product.id} {...product} />
               )
            ))}
        </div>
    );
}