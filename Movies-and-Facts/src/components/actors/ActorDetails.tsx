import { Card, CardActions, CardContent, IconButton } from "@mui/material";
import { Container } from "@mui/system";
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { BACKEND_API_URL } from "../../constants";
import { Actor } from "../../models/Actor";
import EditIcon from "@mui/icons-material/Edit";
import DeleteForeverIcon from "@mui/icons-material/DeleteForever";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";

export const ActorDetails = () => {
	const { actorId } = useParams();
	const [actor, setActor] = useState<Actor>();

	useEffect(() => {
		const fetchActor = async () => {
			// TODO: use axios instead of fetch
			// TODO: handle errors
			// TODO: handle loading state
			const response = await fetch(`${BACKEND_API_URL}/actors/${actorId}`);
			const actor = await response.json();
			setActor(actor);
		};
		fetchActor();
	}, [actorId]);

	return (
		<Container>
			<Card>
				<CardContent>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/actors`}>
						<ArrowBackIcon />
					</IconButton>{" "}
					<h1>Actor Details</h1>
					<p>Actor Name: {actor?.name}</p>
					<p>Actor Birth Date: {actor?.birth_date}</p>
					<p>Actor Films: {actor?.films}</p>
					<p>Actor Height: {actor?.height}</p>
					<p>Actor Married: {actor?.married}</p>
				</CardContent>
				<CardActions>
					<IconButton component={Link} sx={{ mr: 3 }} to={`/actors/${actorId}/edit`}>
						<EditIcon />
					</IconButton>

					<IconButton component={Link} sx={{ mr: 3 }} to={`/actors/${actorId}/delete`}>
						<DeleteForeverIcon sx={{ color: "red" }} />
					</IconButton>
				</CardActions>
			</Card>
		</Container>
	);
};