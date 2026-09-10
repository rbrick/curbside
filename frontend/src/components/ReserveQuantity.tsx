

export interface ReserveQuantityProps {
    id: number;
    available_quantity: number;

    getReservedQuantity: () => number;
    setReservedQuantity: (quantity: number) => void;
}

export default function ReserveQuantity({ id, available_quantity, getReservedQuantity, setReservedQuantity }: ReserveQuantityProps) {
    const increment = () => { setReservedQuantity(Math.min(getReservedQuantity() + 1, available_quantity)) };
    const decrement = () => { setReservedQuantity(Math.max(getReservedQuantity() - 1, 0)) };

    const onReserve = (amount: number) => {
        console.log(`Reserving ${amount} of product with id ${id}`);

        if (amount <= 0) {
            alert("invalid amount. must be greater than 0");
        }
    };

    return (
        <div className="flex flex-col m-2 gap-2">
            <p className="justify-center text-center">{getReservedQuantity()}</p>
            <div className="flex flex-row gap-2 justify-center">
                <button className="bg-green-500 text-white p-2 rounded" onClick={increment}>+</button>
                <button className="bg-red-500 text-white p-2 rounded" onClick={decrement}>-</button>
            </div>
            <button className="bg-blue-500 text-white p-2 rounded" onClick={() => onReserve(getReservedQuantity())}>Reserve</button>
        </div>
    );
}