using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace GraphBFS
{
	class Program
	{
		static void Main(string[] args)
		{
            var adjacency_list2 = new List<List<int>>();
            adjacency_list2.Add(new List<int>() { 0, 1, 2, 3, 4 });
            adjacency_list2.Add(new List<int>() { 1, 0, 2, 6 });
            adjacency_list2.Add(new List<int>() { 2, 0, 1, 3 });
            adjacency_list2.Add(new List<int>() { 3, 0, 2, 7 });
            adjacency_list2.Add(new List<int>() { 4, 0, 5 });
            adjacency_list2.Add(new List<int>() { 5, 6, 7 });
            adjacency_list2.Add(new List<int>() { 6, 5, 1 });
            adjacency_list2.Add(new List<int>() { 7, 5, 3 });

            var result2 = BFS(adjacency_list2);
            var expected = new List<int>() { 0, 1, 2, 3, 4, 6, 5, 7 };
            Console.WriteLine("Result: " + String.Join(',', result2));
            Console.ReadKey();
		}

        static IEnumerable<int> BFS(IEnumerable<IEnumerable<int>> graph) {

            if (graph is null || graph.Count() == 0)
                return new List<int>();

            Console.WriteLine("Graph: " + GraphToString(graph));

            var visited = new HashSet<int>();
            var queue = new Queue<int>();
            queue.Enqueue(graph.First().First());
            var result = new List<int>();
            int iteration = 0;

            while (queue.Count() != 0)
            {
                Console.WriteLine($"{++iteration}. Queue: " + String.Join(',', queue.ToArray()));
                Console.WriteLine($"   Visited: " + String.Join(',', visited.ToArray()));

                var node = queue.Dequeue();

                if (!visited.Contains(node))
                {
                        visited.Add(node);
                        result.Add(node);
                }

                var list = graph.Where(x => x.First() == node).First();

                foreach (var adjacent in list)
                {
                    if (!visited.Contains(adjacent))
                        queue.Enqueue(adjacent);
                }
            }

            return result;
       }

        private static string GraphToString<T>(IEnumerable<IEnumerable<T>> graph)
        {
            StringBuilder stringBuilder = new StringBuilder();

            stringBuilder.Append("[");
            foreach (var x in graph)
            {
                stringBuilder.Append(" [");
                stringBuilder.AppendJoin(",", x);
                stringBuilder.Append("], ");
            }
            stringBuilder.Append(']');
            return stringBuilder.ToString();
        }
    }
}
