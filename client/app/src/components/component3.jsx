import React, {useState, useEffect} from 'react';
import axios from 'axios';



const Component3 = () => {


    const [Data, SetData] = useState([]);

    const FetchInnerJoin = async() => {

        try{

            const response = await axios.get();

        }catch(error){
            console.log(`error in the Component3 @FetchInnerJoin function, ${error}`);
        }
    }

    return (
        <>
            <h1>This is a Compoent3</h1>
        </>
    )

}


export default Component3;