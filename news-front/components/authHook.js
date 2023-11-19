"use client";
import React, { useState, useEffect, useContext, createContext } from 'react'
import { useMutation, useQuery } from 'react-query'

const authContext = createContext();

export function AuthProvider({ children }) {
  const auth = useProvideAuth()
  return <authContext.Provider value={auth}>{children}</authContext.Provider>
}

export const useAuth = () => {
  return useContext(authContext)
}

function useProvideAuth() {
    const [news, setNews] = useState(null);
    const [newsId, setNewsId] = React.useState(0);
    const [fetchFailed, setFetchFailed] = useState(false);

    /**
     * User fetching
     */
    const newsReq = useQuery({ 
        queryKey: ['news', newsId], 
        cacheTime: 0, 
        retry: false, 
        queryFn: async()=>{
            if(fetchFailed) return;

            const res = await fetch(`/news/${newsId}`);
            const me = await res.json();
            return me;
        }, 
        onSuccess: (data) => {
            if(newsReq.data || !data) return;
            const newNews = {...newsReq};
            setNews(newNews);
        },
        onError: (err) => {
            setFetchFailed(true);
        }
    });

    return {
        news
    }
}