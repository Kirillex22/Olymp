using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.CompilerServices;

namespace WORM
{
    internal class Program
    {
        static int BellmanFord(int[,] graph, int V, int src, int destination){
            int[] dis = new int[V];
            int E = 2 * (V - 1);

            for (int i = 0; i < V; i++)
                dis[i] = 9999999;

            dis[src] = 0;
            for (int i = 0; i < V - 1; i++){
                for (int j = 0; j < E; j++){
                    dis[graph[j, 1]] = Math.Min(dis[graph[j, 1]], dis[graph[j, 0]] + graph[j, 2]);
                    dis[graph[j, 0]] = Math.Min(dis[graph[j, 0]], dis[graph[j, 1]] + graph[j, 2]);
                }
            }
            return dis[destination];
        }
        static void Main(string[] args){
            string path;
            Console.WriteLine("введите кол-во тестов");
            int value = int.Parse(Console.ReadLine());
            Console.Clear();
            string[] nums;
            int min;
            int temp;
            int newspot = 0;
            for (int z = 1; z < value + 1; z++){
                if (z < 10)
                    path = "C:\\Users\\ziabr\\Downloads\\tests\\tests\\input_s1_0" + Convert.ToString(z) + ".txt";
                else
                    path = "C:\\Users\\ziabr\\Downloads\\tests\\tests\\input_s1_" + Convert.ToString(z) + ".txt";

                List<string[]> lines = new List<string[]>();

                using (StreamReader reader = new StreamReader(path)){
                    string? line;
                    while ((line = reader.ReadLine()) != null)
                        lines.Add(line.Split(' '));
                }
                int distance = 0;
                nums = lines[0];
                int n = int.Parse(nums[0]);
                int m = int.Parse(nums[1]);
                int[,] branches = new int[2 * n, 3];
                List<int[]> apples = new List<int[]>();

                for (int i = 0; i < n; i++){
                    string[] rib = lines[i + 1];
                    int k = int.Parse(rib[0]);
                    int w = int.Parse(rib[1]);
                    int[] branch = { k, i + 1, w };
                    int[] branch_1 = { i + 1, k, w };
                    for (int j = 0; j < 3; j++){
                        branches[i, j] = branch[j];
                        branches[i + 1, j] = branch_1[j];
                    }
                }

                for (int i = 0; i < m; i++){
                    string[] apple = lines[i + 1 + n];
                    int[] apple_1 = { int.Parse(apple[0]), int.Parse(apple[1]) };
                    apples.Add(apple_1);
                }

                List<int[]> apples_copy = new List<int[]>();
                foreach (int[] i in apples)
                    apples_copy.Add(i);

                nums = lines[lines.Count - 1];
                int worms_spot = int.Parse(nums[0]);
                int itsok = int.Parse(nums[1]);

                foreach (int[] i in apples_copy){
                    if (i[1] < itsok)
                        apples.Remove(i);
                }

                apples_copy.Clear();
                foreach (int[] i in apples)
                    apples_copy.Add(i);

                while (apples.Count > 0){
                    min = 9999999;
                    foreach (int[] i in apples){
                        temp = BellmanFord(branches, n + 1, worms_spot, i[0]);
                        if (temp < min){
                            min = temp;
                            newspot = i[0];
                        }
                    }
                    distance += min;
                    foreach (int[] i in apples)
                        if (i[0] == newspot){
                            apples.Remove(i);
                            break;
                        }
                    worms_spot = newspot;
                    //Console.WriteLine("min: {0} | current_distance: {1} | worms_spot: {2}", min, distance, worms_spot);
                }
                if (z < 10)
                    path = "C:\\Users\\ziabr\\Downloads\\tests\\tests\\output_s1_0" + Convert.ToString(z) + ".txt";
                else
                    path = "C:\\Users\\ziabr\\Downloads\\tests\\tests\\output_s1_" + Convert.ToString(z) + ".txt";

                using (StreamReader reader = new StreamReader(path)){
                    string? line;
                    line = reader.ReadLine();
                    if (int.Parse(line) == distance)
                        Console.WriteLine("{0}\t[+]", z);
                    else
                        Console.WriteLine("{0}\t[-]", z);
                }
            }
        }
    }
}
