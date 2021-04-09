import java.util.*;
import java.io.*;


public class pioneerAndProsper {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static PrintWriter pr = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
	static StringTokenizer st;
	static int []ay =  {1,  2,  3,  4,  5,  6,  7,  8,  15, 9,  10, 11, 40, 39,  32, 17, 19, 30, 33};
	static int []bee = {22, 21, 20, 19, 18, 17, 16, 15, 43, 14, 13, 40, 37, 41,  28, 23, 27, 27, 43};
	static TreeSet<edge> [] adj;
	static int n;
	static int m;
	static double tpd = 0.3;
	
	public static void main(String[] args) throws IOException {
		n = readInt(); m = readInt();
		adj = new TreeSet[n+1];
		for (int i=1;i<=n;i++) adj[i]=new TreeSet <edge> ();
		
		for (int i=1;i<=m;i++) {
			int a = readInt(), b = readInt(), c = readInt();
			adj[a].add(new edge(b,c));
			adj[b].add(new edge(a,c));
		}
		
		int totdis=0;
		for (int e=1;e<n;e++)
			totdis+=djs(e);
		
		System.out.println("Orig: " + totdis *tpd + " mins");
		
		int best=Integer.MAX_VALUE;
		int x=0;
		int y=0;
		
		for (int i=0;i<ay.length;i++) {
			totdis=0;
			adj[ay[i]].add(new edge(bee[i],0));
			adj[bee[i]].add(new edge(ay[i],0));
			for (int e=1;e<n;e++) {
				totdis+=djs(e);
			}
			if (totdis<best) {
				best=totdis;
				x=ay[i];
				y=bee[i];
			}
			adj[ay[i]].remove(new edge(bee[i],0));
			adj[bee[i]].remove(new edge(ay[i],0));
		}
		
		System.out.println("Best: "+ best*tpd + " mins");
		System.out.println("a: "+ x+" b: "+y);
	}
	public static int djs (int s) {
		int [] dist = new int [n+1];
		for (int i=0;i<=n;i++) dist[i]=2000;
		
		dist[s]=0;

		PriorityQueue<edge> pq = new PriorityQueue<edge>();

		pq.add(new edge(s,0));
		edge cur;

		while(pq.isEmpty()==false) {
			cur=pq.poll();

			for (edge q:adj[cur.v]) {
				if (dist[q.v]>dist[cur.v]+q.w) {
					dist[q.v]=dist[cur.v]+q.w;
					pq.add(new edge (q.v, dist[q.v]));
				}
			}
		}
		
		return dist[n];
	}
	static class edge implements Comparable <edge> {
		int v,w;
		edge(int f,int s) {
			v = f; w = s;
		}
		public int compareTo (edge x) { 
			if (w!=x.w) {
				return w-x.w;
			}
			else {
				return v-x.v;
			}
		}
	}
	static String next() throws IOException {
		while (st == null || !st.hasMoreTokens())
			st = new StringTokenizer(br.readLine().trim());
		return st.nextToken();
	}

	static long readLong() throws IOException {
		return Long.parseLong(next());
	}

	static int readInt() throws IOException {
		return Integer.parseInt(next());
	}

	static double readDouble() throws IOException {
		return Double.parseDouble(next());
	}

	static char readCharacter() throws IOException {
		return next().charAt(0);
	}

	static String readLine() throws IOException {
		return br.readLine().trim();
	}
}
