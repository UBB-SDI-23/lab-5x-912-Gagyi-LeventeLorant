import { CssBaseline, Container, Typography } from "@mui/material";
import React from "react";

export const AppHome = () => {
	return (
		<React.Fragment>
			<CssBaseline />

			<Container maxWidth="xl">
				<Typography variant="h1" component="h1" textAlign={"center"} gutterBottom>
					Welcome to the estanoshing world of movies!
				</Typography>
			</Container>
		</React.Fragment>
	);
};