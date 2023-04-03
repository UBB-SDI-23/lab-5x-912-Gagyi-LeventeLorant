import { useEffect, useState } from "react"
import { Film } from "../../models/Film";

export const FilmsShowAll = () => {
    const [films, setFilms] = useState([]);


    useEffect(() => {
    fetch("http://ec2-13-48-126-143.eu-north-1.compute.amazonaws.com/films/")
    .then((res) => res.json())
    .then((data) => setFilms(data));
    }, []);



    if(films.length === 0){
      return <div>No films</div>
    }
    return (
      <div className="App">
        <h1>Films list</h1>
        <table>
            <tr>
                <th>#</th>
                <th>Film name</th>
                <th>Profit</th>
                <th>Rating</th>
            </tr>
            {films.map((film : Film, index) => (
                <tr>
                    <td>{index}</td>
                    <td>{film.name}</td>
                    <td>{film.profit}</td>
                    <td>{film.rating}</td>
                </tr>
            ))
            }
        </table>
      </div>
    )
  }
  