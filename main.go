package main

import (
  "log"
  "net/http"
  "time"
  "fmt"
  "github.com/gorilla/mux"
)

func main() {
  r := mux.NewRouter()
  r.PathPrefix("/app").Handler(http.StripPrefix("/app/", http.FileServer(http.Dir("./assets/"))))

  r.HandleFunc("/api/time", func(w http.ResponseWriter, r *http.Request) {
    currentTime := time.Now().Format("15:04:05")
    fmt.Fprintf(w, "Current server time is: %s", currentTime)
  }).Methods("GET")

  log.Println("Listening on port...")
  srv := &http.Server{
    Handler:      r,
    Addr:         "127.0.0.1:8000",
    WriteTimeout: 15 * time.Second,
    ReadTimeout:  15 * time.Second,  // RenderTimeout should be ReadTimeout
  }


  log.Fatal(srv.ListenAndServe())
}
