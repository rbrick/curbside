import ReserveQuantity from "./ReserveQuantity";
import { useState } from "react";
export interface ProductProps {
    id: number;
    name: string;
    available_quantity: number;
    total_quantity: number;
    price_cents: number;
}



export default function Product({ id, name, available_quantity, total_quantity, price_cents }: ProductProps) {
  const [reservedQuantity, setReservedQuantity] = useState(0);
  

  return (
    <div className="flex flex-col m-2 border-black border p-2">
      <h2>{name}</h2>
      <p>Available Quantity: {available_quantity}</p>
      <p>Total Quantity: {total_quantity}</p>
      <p>Price: ${(price_cents / 100).toFixed(2)}</p>
      <ReserveQuantity id={id}  available_quantity={available_quantity} getReservedQuantity={() => reservedQuantity} setReservedQuantity={setReservedQuantity} />
    </div>
  );
}