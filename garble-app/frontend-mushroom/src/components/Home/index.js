import React, { useEffect, useRef, useState } from 'react';
import { withStyles } from '@material-ui/core';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import CircularProgress from '@material-ui/core/CircularProgress';

import DataService from "../../services/DataService";
import styles from './styles';

const SummaryText = ({summary}) => {
  if (summary) { 
    return <div>{summary.summary}</div>
  } else { 
    return <div style={{marginLeft: 'auto', marginRight: 'auto', width: '13rem'}}>2. Get short summary of audio.</div>
  }
}

const Home = (props) => {
  const { classes } = props;

  console.log("================================== Home ======================================");

  const inputFile = useRef(null);

  // Component States
  const [audio, setAudio] = useState(null);
  const [summary, setSummary] = useState(null);
  const [isLoading, setIsLoading] = useState(false); 

  // Setup Component
  useEffect(() => {

  }, []);

  // Handlers
  const handleAudioUploadClick = () => {
    inputFile.current.click();
  }
  const handleOnChange = async (event) => {
    setIsLoading(true);
    console.log(event.target.files);
    setAudio(URL.createObjectURL(event.target.files[0]));

    var formData = new FormData();
    formData.append("file", event.target.files[0]);
    await DataService.Predict(formData)
      .then(function (response) {
        setSummary(response.data);
      }); 
    setIsLoading(false);
  }

  return (
    <div className={classes.root}>
      <main className={classes.main}>
        <Container maxWidth="md" className={classes.container}>
          <Grid container spacing={2}>
            <Grid item xs={6}>
              <h3 className={classes.centerElement}>Audio</h3>
              <div className={classes.dropzone} onClick={() => handleAudioUploadClick()}>
                <input
                  type="file"
                  accept="audio/*"
                  className={classes.fileInput}
                  ref={inputFile}
                  onChange={(event) => handleOnChange(event)}
                />
                <div>{audio && <audio controls src={audio} />}</div>
                <div className={classes.help}>1. Click to upload audio file.</div>
              </div>
            </Grid>
            <Grid item xs={6}>
              <h3 className={classes.centerElement}>Summary</h3>
              {isLoading ? <div className={classes.centerElement}><CircularProgress/></div>: <SummaryText summary={summary} />}
            </Grid>
          </Grid>
        </Container>
      </main>
    </div>
  );
};

export default withStyles(styles)(Home);