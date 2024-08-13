import React, {useState, useEffect} from 'react';
import axios from 'axios';



const Component3 = () => {


    const user_id = 1001;

    const [Data, SetData] = useState([]);

    const FetchInnerJoin = async() => {

        try{

            const response = await axios.get(`http://127.0.0.1:8000/user/show/orders/${user_id}`);
            console.log(response.data);
            SetData(response.data);

        }catch(error){
            console.log(`error in the Component3 @FetchInnerJoin function, ${error}`);
        }
    }


    useEffect(() => {

        FetchInnerJoin();

    }, [])

    return (
        <>
            <h1>This is a Compoent3</h1>

            {Data.map((orderObj) => (
                <div>
                    <p>id : {orderObj.id}</p>
                    <p>product: {orderObj.product}</p>
                    <p>user: {orderObj.user}</p>
                    <p>username : {orderObj.user__username}</p>
                    <p>age : {orderObj.user__age}</p>
                    <p>gender : {orderObj.user__gender}</p>
                    <p>email : {orderObj.user__email}</p>
                </div>
            ))}
        </>
    )

}


export default Component3;