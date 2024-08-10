import React, { useState, useEffect } from 'react'
import axios from 'axios';

const Component1 = () => {

    const [Data, SetData] = useState(null);

    const fetchData = async() => {
        
        try{

            // const response = {
            //     "data" : 'hello world'
            // };

            
            // SetData(response);


            const response = await axios.get(`http://127.0.0.1:8000/user/dev/`)
            console.log(response);
            console.log(response.data);
            SetData(response.data);

        }catch(error){
            console.log(`Error in Component1 @fetchData function,  ${error}`)
        }

    }


    useEffect(() => {
        fetchData()
        console.log('useffect logging');
    }, [])


    return (
        <>
            <h1>This is Component1</h1>
            {Data && (<h3>{Data.developer_email}</h3>)}
        </>
    )
}

export default Component1;