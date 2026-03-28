from fastapi import FastAPI, HTTPException, Query
from pydantic import HttpUrl
from yt_functions import get_audio_stream_url, get_song_details

app = FastAPI()

@app.get("/getMusicDetails")
async def get_music(url: HttpUrl = Query(..., description="The URL of the music file or stream")):
    try:
        details = get_song_details(str(url))
        stream = get_audio_stream_url(str(url))

        return {
            "status": "success",
            "data": {
                "url": str(url),
                **details,
                **stream
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)